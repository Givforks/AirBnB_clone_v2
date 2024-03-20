import unittest
import MySQLdb
import subprocess


class TestCreateState(unittest.TestCase):
    def setUp(self):
        self.db = MySQLdb.connect(
            "localhost",
            "hbnb_test",
            "hbnb_test_pwd",
            "hbnb_test_db"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT COUNT(*) FROM states")
        self.initial_count = self.cursor.fetchone()[0]

    def test_create_state(self):
        # Replace this with the actual command to run your console script
        subprocess.run([
            "python",
            "console.py",
            "create",
            "State",
            "name='California'"
        ])
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]
        self.assertEqual(final_count, self.initial_count + 1)

    def tearDown(self):
        self.db.close()


if __name__ == '__main__':
    unittest.main()
