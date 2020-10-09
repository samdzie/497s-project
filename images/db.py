import sqlite3
import random
###Creating Connection with images database -> images.db
try:
    sqliteConnection = sqlite3.connect('images.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")


###Creating images table -> images_table
try:
    sqliteConnection = sqlite3.connect('images.db')
    sqlite_create_table_query = '''CREATE TABLE images_table ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

# def add_group_icon(self, image):
#         """Add a group icon to the database and return a unique ID."""
def add_group_icon(image_id, name, photo):
    try:
        sqliteConnection = sqlite3.connect('images.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")


        sqlite_insert_blob_query = """ INSERT INTO images_table
                                  (id, name, photo) VALUES (?, ?, ?)"""

        emptyPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (image_id, name, emptyPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

#####ASSIGNING A NEW RANDOM KEY#######
# def add_group_icon(name, photo):
#     try:
#         sqliteConnection = sqlite3.connect('images.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         image_id = random.randint(0, 1000000)
#         #print( image_id + "---------------------")
#         sqlite_insert_blob_query = """ INSERT INTO images_table
#                                   (id, name, photo) VALUES (?, ?, ?)"""

#         emptyPhoto = convertToBinaryData(photo)
#         # Convert data into tuple format
#         data_tuple = (image_id, name, emptyPhoto)
#         cursor.execute(sqlite_insert_blob_query, data_tuple)
#         sqliteConnection.commit()
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to insert blob data into sqlite table", error)
#     finally:
#         if (sqliteConnection):
#             sqliteConnection.close()
#             print("the sqlite connection is closed")
#     return image_id

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

# def get_group_icon(self, image_id):
#     """Return a group icon given its unique ID."""

def get_group_icon(image_id):
    try:
        sqliteConnection = sqlite3.connect('images.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from images_table where id = ?"""
        cursor.execute(sql_fetch_blob_query, (image_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]

            print("Storing employee image and resume on disk \n")
            photoPath = "" + name + ".jpg"
            writeTofile(photo, photoPath)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

add_group_icon(1, "Smith", "source.png")
add_group_icon(2, "David", "less.png")

# add_group_icon("Smith", "source.png")
# add_group_icon( "David", "less.png")

get_group_icon(1)
get_group_icon(2)

#( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL)
