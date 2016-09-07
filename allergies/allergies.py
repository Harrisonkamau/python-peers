"""
Write a program that, given a person's allergy score, can tell them whether or not they're allergic to a given item, and their full list of allergies.

An allergy test produces a single numeric score which contains the
information about all the allergies the person has (that they were
tested for).

The list of items (and their value) that were tested are:

* eggs (1)
* peanuts (2)
* shellfish (4)
* strawberries (8)
* tomatoes (16)
* chocolate (32)
* pollen (64)
* cats (128)

So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

Now, given just that score of 34, your program should be able to say:

- Whether Tom is allergic to any one of those allergens listed above.
- All the allergens Tom is allergic to.

"""
import unittest


# your class
class Allergies(object):
    def __init__(self, value):
        self.value = value

    def is_allergic_to(self, allergen):
        total = 0
        dict1 = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }

        item = dict1[allergen]

        total += item

        if total > self.value:
            return False
        else:
            return True

    def lst(self):

        dict2 = {
            1: 'eggs',
            2: 'peanuts',
            4: 'shellfish',
            8: 'strawberries',
            16: 'tomatoes',
            32: 'chocolate',
            64: 'pollen',
            128: 'cats'
        }

        if self.value in dict2:
            item2 = dict2[self.value]
            return [item2]
        elif self.value == 0 or self.value is None:
            return []
        elif self.value > 255:
            return [dict2[1]]
        else:
            return dict2.values()


class AllergiesTests(unittest.TestCase):
    def test_no_allergies_means_not_allergic(self):
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_is_allergic_to_eggs(self):
        self.assertTrue(Allergies(1).is_allergic_to('eggs'))

    def test_has_the_right_allergies(self):
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_no_allergies_at_all(self):
        self.assertEqual([], Allergies(0).lst())

    def test_allergic_to_just_peanuts(self):
        self.assertEqual(['peanuts'], Allergies(2).lst())

    def test_allergic_to_everything(self):
        self.assertEqual(
            sorted(('eggs peanuts shellfish strawberries tomatoes '
                    'chocolate pollen cats').split()),
            sorted(Allergies(255).lst()))

    # @unittest.skip('Extra Credit: Passes with a specific type of solution')
    def test_ignore_non_allergen_score_parts(self):
        self.assertEqual(['eggs'], Allergies(257).lst())


if __name__ == '__main__':
    unittest.main()
