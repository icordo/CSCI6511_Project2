import CSPColoring
import unittest


class TestSampleFiles(unittest.TestCase):

    def testCase_1(self):
        print("Test 1 -----INITIATED")
        output = CSPColoring.CSPColoring("test_1.txt")
        self.assertNotEqual(len(output), 0)
        print("Test 1 -----COMPLETE")
        print("Result:")
        print(output[0])
        print()

    def testCase_2(self):
        print("Test 2 -----INITIATED")
        output = CSPColoring.CSPColoring("test_2.txt")
        self.assertNotEqual(len(output), 0)
        print("Test 2 -----COMPLETE")
        print("Result:")
        print(output[0])
        print()

    def testCase_3(self):
        print("Test 3 -----INITIATED")
        output = CSPColoring.CSPColoring("test_3.txt")
        self.assertNotEqual(len(output), 0)
        print("Test 3 -----COMPLETE")
        print("Result:")
        print(output[0])
        print()

    def testCase_4(self):
        print("Test 4 -----INITIATED")
        output = CSPColoring.CSPColoring("test_4.txt")
        self.assertNotEqual(len(output), 0)
        print("Test 4 -----COMPLETE")
        print("Result:")
        print(output[0])
        print()

    def testCase_5(self):
        print("Test 5 -----INITIATED")
        output = CSPColoring.CSPColoring("test_5.txt")
        self.assertNotEqual(len(output), 0)
        print("Test 5 -----COMPLETE")
        print("Result:")
        print(output[0])
        print()

    def testCase_6(self):
        print("Test 6 -----INITIATED")
        output = CSPColoring.CSPColoring("test_6.txt")
        self.assertNotEqual(len(output), 0)
        print("Test 6 -----COMPLETE")
        print("Result:")
        print(output[0])
        print()

    def testCase_7(self):
        print("Test 7 -----INITIATED")
        output = CSPColoring.CSPColoring("test_7.txt")
        self.assertEqual(len(output), 0)
        print("Test 7 -----COMPLETE")
        print("Result: ")
        print("No Solution available for this configuration\n")

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
