````markdown
# NoSQL

This project introduces **NoSQL** databases, specifically focusing on **MongoDB**. You will learn the fundamental differences between SQL and NoSQL, how to perform basic CRUD operations (Create, Read, Update, Delete) using the MongoDB shell, and how to interact with MongoDB using Python and `PyMongo`.


## 📚 Resources

**Read or watch:**

* [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
* [What is NoSQL ?](https://www.youtube.com/watch?v=qI_g07C_Q5I)
* [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
* [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
* [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
* [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
* [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
* [The mongo Shell](https://www.mongodb.com/docs/manual/mongo/)

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* What **NoSQL** means
* What is the difference between **SQL** and **NoSQL**
* What is **ACID**
* What is a **document storage**
* What are **NoSQL types**
* What are the benefits of a NoSQL database
* How to **query** information from a NoSQL database
* How to **insert/update/delete** information from a NoSQL database
* How to use **MongoDB**

---

## ⚙️ Requirements

### MongoDB Command File
* **Environment:** All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **MongoDB** (version 4.4).
* **File Ending:** All your files should end with a new line.
* **Comments:** The first line of all your files should be a comment: `// my comment`.
* **README:** A `README.md` file, at the root of the folder of the project, is mandatory.
* **Length:** The length of your files will be tested using `wc`.

### Python Scripts
* **Environment:** All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.9) and `PyMongo` (version 4.8.0).
* **File Ending:** All your files should end with a new line.
* **Shebang:** The first line of all your files should be exactly `#!/usr/bin/env python3`.
* **Style:** Your code should use the `pycodestyle` style (version 2.5.*).
* **Documentation:** All modules and functions should have documentation strings.
* **Import Guard:** Your code should not be executed when imported (by using `if __name__ == "__main__":`).

---

## 💻 Installation & Environment

### Install MongoDB 4.4 in the sandbox (Ubuntu 22.04)

**1. Install the missing `libssl1.1` dependency:**
```bash
echo "deb [http://security.ubuntu.com/ubuntu](http://security.ubuntu.com/ubuntu) focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install -y libssl1.1
sudo rm /etc/apt/sources.list.d/focal-security.list
sudo apt update
````

**2. Add the MongoDB 4.4 repository and key:**

```bash
curl -fsSL [https://www.mongodb.org/static/pgp/server-4.4.asc](https://www.mongodb.org/static/pgp/server-4.4.asc) | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] [https://repo.mongodb.org/apt/ubuntu](https://repo.mongodb.org/apt/ubuntu) focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
```

**3. Install MongoDB 4.4 packages:**

```bash
sudo apt install -y mongodb-org
```

**4. Prepare required directories and permissions:**

```bash
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb
```

**5. Start `mongod`:**

```bash
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &
```

**Verification:**

```bash
mongod --version
# Expected output should show v4.4.xx
```

-----

## 📂 Tasks

### 0\. List all databases

Write a script that lists all databases in MongoDB.

  * **File:** `0-list_databases`

### 1\. Create a database

Write a script that creates or uses the database `my_db`.

  * **File:** `1-use_or_create_database`

### 2\. Insert document

Write a script that inserts a document in the collection `school`.

  * The document must have one attribute `name` with value “Holberton school”.
  * The database name will be passed as option of `mongo` command.
  * **File:** `2-insert`

### 3\. All documents

Write a script that lists all documents in the collection `school`.

  * The database name will be passed as option of `mongo` command.
  * **File:** `3-all`

### 4\. All matches

Write a script that lists all documents with `name="Holberton school"` in the collection `school`.

  * The database name will be passed as option of `mongo` command.
  * **File:** `4-match`

### 5\. Count

Write a script that displays the number of documents in the collection `school`.

  * The database name will be passed as option of `mongo` command.
  * **File:** `5-count`

### 6\. Update

Write a script that adds a new attribute to a document in the collection `school`.

  * The script should update only document with `name="Holberton school"` (all of them).
  * The update should add the attribute `address` with the value “972 Mission street”.
  * The database name will be passed as option of `mongo` command.
  * **File:** `6-update`

### 7\. Delete by match

Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.

  * The database name will be passed as option of `mongo` command.
  * **File:** `7-delete`

### 8\. List all documents in Python

Write a Python function that lists all documents in a collection.

  * **Prototype:** `def list_all(mongo_collection):`
  * Return an empty list if no document in the collection.
  * `mongo_collection` will be the `pymongo` collection object.
  * **File:** `8-all.py`

### 9\. Insert a document in Python

Write a Python function that inserts a new document in a collection based on `kwargs`.

  * **Prototype:** `def insert_school(mongo_collection, **kwargs):`
  * `mongo_collection` will be the `pymongo` collection object.
  * Returns the new `_id`.
  * **File:** `9-insert_school.py`

### 10\. Change school topics

Write a Python function that changes all topics of a school document based on the name.

  * **Prototype:** `def update_topics(mongo_collection, name, topics):`
  * `mongo_collection` will be the `pymongo` collection object.
  * `name` (string) will be the school name to update.
  * `topics` (list of strings) will be the list of topics approached in the school.
  * **File:** `10-update_topics.py`

### 11\. Where can I learn Python?

Write a Python function that returns the list of schools having a specific topic.

  * **Prototype:** `def schools_by_topic(mongo_collection, topic):`
  * `mongo_collection` will be the `pymongo` collection object.
  * `topic` (string) will be topic searched.
  * **File:** `11-schools_by_topic.py`

### 12\. Log stats

Write a Python script that provides some stats about Nginx logs stored in MongoDB.

  * **Database:** `logs`
  * **Collection:** `nginx`
  * **Display:**
      * First line: `x logs` where `x` is the number of documents in this collection.
      * Second line: `Methods:`
      * 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order.
      * One line with the number of documents with `method=GET` and `path=/status`.
  * **File:** `12-log_stats.py`

-----

## 📋 Repository Information

  * **GitHub repository:** `holbertonschool-webstack`
  * **Directory:** `nosql`

<!-- end list -->

```
```