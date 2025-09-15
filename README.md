> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# HW 1: Housing Priority Calculator

## Learning Outcomes
- Practice writing tests
- Practice designing functions in Python with type annotations, documentation, and tests
- Developing classes in Python with proper separation of concerns
- Understanding object-oriented design principles
- Reading and writing text files

## Overview
Welcome to your first programming assignment of the semester! In this assignment you will be building a housing "priority score" engine in Python that decides who gets the first pick of campus housing. You'll dive into human-centered design—chatting with users, uncovering their needs, and iterating on your plan—while mastering Python basics: grabbing input, crafting if/elif/else logic, performing arithmetic, and tallying up points.

This assignment is based on this [Nifty Assignment](http://nifty.stanford.edu/2020/peck-decision-makers/).

## NOTE
Although this assignment primarily focuses on writing tests before implementation, it should be general practice to formalize and think about concrete examples first before writing code.


This assignment introduces you to **object-oriented programming** by separating functionality into distinct classes:

### File Structure
1. **`question_asker.py`** - Contains the `HousingQuestionAsker` class (skeleton provided)
   * `ask_class_year()`
   * `ask_graduation_status()`
   * `ask_credits_earned()`
   * `ask_additional_questions()`

2. **`priority_calculator.py`** - Contains the `HousingPriorityCalculator` class (skeleton provided)
   * `points_for_class_year(year)`
   * `points_for_graduation(is_graduating)`
   * `points_for_credits(credits)`
   * `points_for_additional_questions(responses)`
   * `calculate_total_score(year, is_graduating, credits, additional_responses)`

3. **`hw1.py`** - Main orchestration file (skeleton provided)
   * `calculate_score()` - coordinates both classes
   * `main()` - entry point

## Your Tasks:

### Part 1: Understand the purpose of each class/function.
Read through the files in the src directory and understand how they are expected to work together.

Do not think about how to implement these functions/classes yet, but think about how the different classes interact with each other.


Note: In the handout files, if you have pylint setup correctly, vscode will show you some errors/informational comments about unused imports or unused variables or unnecessary pass statements. You may ignore these for now as they will go away once you start completing the hw. Do not get rid of the imports or any starter code assuming it is unused, you will need it later! 


### Part 2: Design Your Scoring System

Based on their inputs to the questions asked, students receive a score that is used in the system to provide housing. Higher scores means their housing needs are more prioritized. Your tasks are to 

1. **Decide** on your priority-based scoring system for each component:
   - How many points for each class year (1-4)?
   - How many points for graduating vs. not graduating?
   - How many points per credit hour?
   - What additional questions will you ask and how many points each?

   You are free to choose your own scoring system, but you will need to explain why you made those choices. 

2. **Document** your scoring system in `Summary.md` - you'll need this for writing tests that conform to this exact specification!

### Part 3: Complete the tests files in the tests/ directory
 
**Before implementing any methods**, complete all the TODO items in the test files:

Note: Before implementing the functions, you should write tests that specify how they are expected to behave. This is a good practice to follow in general, not just for this assignment, because it forces you to think about different inputs and edge cases independently from how *your* particular implementation might handle them. 


You will notice that some test file names begin with `impl_`. This is because the tests in these files are specific to how you choose to implement this assignment (other valid implementations may fail these tests, and that's okay). 

The tests in file names starting with `test_`, on the other hand, are interface tests (ie. they should pass for any valid implementation). The tests in these files should not be specific to your implementation.

For this assignment, you do not have to worry about segregating your tests into `test_` and `impl_` files, as we have already provided partially written tests in the appropriate files, but pay attention to why the tests have been split this way in the provided handout. 

You must write all interface tests (`test_*.py`) before implementing your functions.
#### 3a. Complete `test_question_asker.py`
- **Write tests** for input validation and error handling
- **Test** invalid input followed by valid input scenarios
- **Use `patch('builtins.input')`** to mock user input

#### 3b. Complete `impl_priority_calculator.py`
- **Write specific test cases** based on your particular scoring system that you previously documented
- **Fill in expected values** for each test method
- **Test edge cases** (invalid years, negative credits, etc.)

#### 3c. Complete `impl_additional_questions.py`
- **Write specific test cases** based on the additional questions that you choose to ask.
- **Fill in expected values** for each test method
- **Test edge cases** (invalid years, uppercase/lowercase input, etc.) 


#### 3d. Complete `impl_hw1.py`
- **Write integration tests** for the main coordination function
- **Use `@patch.object()`** to simulate all inputs and verify totals
- **Test** that graduation questions are only asked for seniors
- **Test** different scenarios (freshman, senior graduating, etc.)

#### 3e. Commit test files

- **IMPORTANT: Make sure you commit what you have to your github repository after writing all the tests, and before starting to implement any of the classes/functions**

- We will be using this commit to check that you have written tests before implementation, so please make sure to commit your tests before the implementation.

- You may try to run your tests now, with `python3 test_runner.py` (more info below on how to run tests). Your tests will fail; this is expected: we haven't gotten to implementing the functionality yet!

### Part 4: Implement Methods according to your test specification
Now implement the actual methods in the order that makes sense:

#### 4a. Implement `question_asker.py`
- **Implement input validation** and error handling
- **Run tests**: `python3 -m pytest test_question_asker.py -v`
- **Handle edge cases** like invalid input followed by valid input

#### 4b. Implement `priority_calculator.py`
- **Implement each method** according to your scoring system
- **Run tests frequently**: `python3 -m pytest test_priority_calculator.py -v`
- **Make sure each test passes** before moving to the next method

#### 4c. Implement `hw1.py`
- **Implement the coordination logic** between both classes
- **Run integration tests**: `python3 -m pytest test_hw1.py -v`
- **Make sure graduation questions are only asked for seniors**

### Part 5: Extending Additional Questions
* **Add exactly two new yes/no prompts** (e.g., older than 23?, honors student?)
* **Update your tests first** to include these new questions, if you haven't done so already
* **Then implement** the functionality to make tests pass
* **Return** a dictionary where each key corresponds to a question and the value is a boolean

### Part 6: Final Testing and Integration
* **Run all tests** to ensure everything passes:
  ```
  python3 test_runner.py
  ```

* **Execute your program (manual testing)**:
  ```
  python3 hw1.py
  ```

  You may run your program directly to manually test that it correctly reads user input in addition to unittesting.

* **Verify** that your inputs produce the expected scores according to your test cases

## Downloading required libraries
Run the following command to install dependencies:

```pip install -r requirements.txt```

For our test_runner.py and generate_coverage_reports.sh files to run, you need to download the required python libraries that are specified in `requirements.txt` with the command above. You don't need to know about these libraries, they are **only** there for our scripts to run properly, but you may take a look at our files if you're interested in seeing how they work. 


## Running Tests
To run your tests, you can use the test_runner.py file we have provided. Run `python3 test_runner.py` to run all tests in the tests/ directory. 

If you try to run the test files directly, you will face an import error due to the way the assignment is structured. DO NOT try to fix this import error, and leave the imports as they are provided in the handout. Othwerwise, the autograder may not be able to run your tests properly, since it uses test_runner.py, and expects tests to execute properly that way. 

While you are completing the test files, you may want to run individual test files at a time, instead of running them all at once. To do this, you can run test_runner.py with the -t option in your terminal to only run tests in the files you specify. Note: the test file names you provide must exist in the tests/ directory, or they won't run. 

Example command to only run tests in test_hw1.py:
```python3 test_runner.py -t test_hw1.py```

You can also run multiple test files by listing the file names after the -t option. 
Example command to run multiple test files: 
```python3 test_runner.py -t test_hw1.py test_priority_calculator.py```

If you just want to run all tests in the tests/ directory, you can run `python3 test_runner.py` omitting the `-t` flag at the end. This will run all test files with the pattern `test_*.py` or `impl_*.py` inside of the tests/ directory. Make sure all your test file names start with either `test_` or `impl_`, or else they will not run.

## Generating Coverage reports

Run the following command in your terminal to generate coverage reports:

```./generate_coverage_reports```

A link to the a html page containing the coverage reports will be produced in the output of the command. You can click on it to view detailed coverage reports. 

These reports indicate how much of your code is being executed by your tests. This is a purely syntactic check, and having full coverage does not necessarily mean your tests are sufficient, but it's a good starting point. You should aim to have full coverage (ie. every line of your code gets executed by your tests)

## Submission Instructions
Push all files to your repository:
   * `question_asker.py` (fully implemented)
   * `priority_calculator.py` (fully implemented)
   * `hw1.py` (fully implemented)
   * `test_question_asker.py` (fully implemented)
   * `test_priority_calculator.py` (fully implemented)
   * `test_hw1.py` (fully implemented)
   * `Summary.md` (completed with scoring rationale)


Good luck!
