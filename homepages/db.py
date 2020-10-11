from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

db = SQLAlchemy()

class HomepageDatabase(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    welcome_message = db.Column(db.String(80), nullable=False)
    about_section = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(10))
    phone_number = db.Column(db.String(10))
    website = db.Column(db.String(10))

    @classmethod
    def create(cls, **kw):
        db.create_all()
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()

    def add_group(self, group_id):
        schema = HomePageSchema()
        initi = HomepageDatabase.query.filter_by(group_id = group_id).first()
        db.session.add(initi)
        db.session.commit()
        return jsonify(schema.dumps(initi))

    def edit_welcome(self, group_id, text):
        edit_wel = HomepageDatabase.query.filter_by(group_id = group_id).first()
        edit_wel.welcome_message = text
        db.session.add(edit_wel)
        db.session.commit()
        return edit_wel.welcome_message

    def edit_about(self, group_id, text):
        edit_ab = HomepageDatabase.query.filter_by(group_id = group_id).first()
        edit_ab.about_section = text
        db.session.add(edit_ab)
        db.session.commit()
        return edit_ab.about_section


    def edit_contact_info(self, group_id, email, phone_number, website):
        edit_contact = HomepageDatabase.query.filter_by(group_id = group_id).first()
        edit_contact.email = email
        edit_contact.phone_number = phone_number
        edit_contact.website = website

        db.session.add(edit_contact)
        db.session.commit()

        about_section = {"email": edit_contact.email, "phone_number": edit_contact.phone_number,
                         "website": edit_contact.website}
        return about_section

class HomePageSchema(SQLAlchemyAutoSchema):
    """Book Marshmallow-SQLAlchemy serialization schema."""
    class Meta:
        model = HomepageDatabase
        load_instance = True

    group_id = auto_field()
    welcome_message = auto_field()
    about_section = auto_field()
    email = auto_field()
    phone_number = auto_field()
    website = auto_field()