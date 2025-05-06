import os
from db import get_db, save_habit, load_habits
from fixtures import generate_test_habits

class TestDatabase:
    def setup_method(self):
        """
        Called before each test – creates a new test database and loads demo habits.
        """
        self.test_db_name = "test_data.db"
        self.db = get_db(self.test_db_name)
        self.demo_habits = generate_test_habits()

    def teardown_method(self):
        """
        Called after each test – deletes the test database file.
        """
        self.db.close()
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_save_and_load_habits(self):
        """
        Tests if habits can be saved to and loaded from the test database.
        """
        for habit in self.demo_habits:
            save_habit(self.db, habit)

        loaded = load_habits(self.db)

        assert len(loaded) == len(self.demo_habits)

        for original, restored in zip(self.demo_habits, loaded):
            assert original.name == restored.name
            assert original.frequency == restored.frequency
            assert len(original.check_ins) == len(restored.check_ins)
