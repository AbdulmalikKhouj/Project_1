import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('posts.db')
        c = conn.cursor()
        
        # Drop the existing posts table if it exists
        c.execute('DROP TABLE IF EXISTS posts')
        
        # Create the posts table
        c.execute('''CREATE TABLE IF NOT EXISTS posts (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        content TEXT,
                        image_path TEXT
                    )''')
        
        # Insert sample data into the posts table
        sample_posts = [
            ('Name', "MSG",'Location'),
            ('Dell', 'Presenting a cutting-edge Dell laptop featuring the latest Intel processor and 16GB RAM, designed for peak performance.', '/static/Image/Dell.jpg'),
            ('Lenova', 'Introducing a high-performance Lenovo laptop, equipped with an Intel processor and 16GB of RAM, ideal for seamless multitasking.', '/static/Image/Lenova.jpg'),
            ('HP', "Here's a sleek HP laptop powered by an Intel processor and boasting 16GB of RAM, ready for any task.", '/static/Image/HP.jpg'),
            ('Mac Laptop', 'This is a Mac laptop with the latest Intel processor and 16GB RAM.', '/static/Image/Mac.jpg')
        ]
        
        c.executemany('''INSERT INTO posts (title, content, image_path) VALUES (?, ?, ?)''', sample_posts)
        
        conn.commit()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
