# Changelog

All notable changes to this project will be documented in this file. 

Grader comments have been added between quotation marks and in brackets. 


## [2.0.1] - 2023-12-03

### 🆕 Added

1.  URL for rendered notebook report in HTML format
2.  CREATIVE COMMONS LICENSE (feedback from Jordan, TA)
3.  scripts that called the function in the command line
4.  Method part which we were missing for [1.0.0]
5.  Test suite information ("I also found that there is an error when I try to run pytest tests/* to test the functions.")
6.  Linked dependencies and dockerfile ("Dependencies: Include a link to the Dockerfile instead of environment.yml (for clarity and full transparency since usage instructions uses docker container)")
7.  Better formatting options for EDA that color by target ("A small note on the EDA portion, for 'previous' parameter, there seems to be only one bar, and the reader might not be able to infer much from this chart.)
8.  Discussed distribution of target variables which was missing earlier ("Not sure if I missed this somewhere, but it will be good for me to know the distribution of target variable in the training dataset.")
9.  Automated model selection ("A small suggestion would be to automate the code in model_selection to choose the best model by itself and returns as 'model_pipeline.pickle.' Otherwise, another idea is to automate and return a click.echo if SVC_bal turns out to not be the best in recall.")
  

### ✅ Fixed 

1. Bugs in functions to make sure all of them are error-free
2. Inconsistency in README.md improved to make sure it's reproducible
3. Improved typos and formatting ("minor spelling error on line 51. Could also mention here to open the Docker Desktop app first (before running docker pull ...)")
4. Improved command prompt scripts to ensure they run without errors ("The issue when running the Python command for python scripts/optimization.py ... is happening for me too.") (" the very last script to run in the cmd line (below # Optimization and Accuracy/Recall Scores) was throwing an error. I tried it both in the container and in the virtual environment and both gave errors. Perhaps, see if the other reviewers were able to get this working, in case it's on my end.)
5. Made minor changes to command prompt commands to ensure they avoid any confusion for users by sharing command for changing to root directory ("line 62: could specify to type in cd work for clarity of where the root of the directory is (when using container)")

### 🐛 Changed

1. Introduction part to make it more thorough
2. Contributing.md to add an option for anyone to make contributions ("detailed and well done. Could add how to contact for general 'seeking support'")


### Removed

- None

## [3.0.0] - 2023-12-06

See all peer reviews for milestone 4 here[`issue#136`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/issues/136)

### Added

- Makefile to automate the data pipeline
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/de5e42e08535d0760173d36491731c4678be1aa7)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/de5e42e08535d0760173d36491731c4678be1aa7)
- Corelation matrix in EDA
("The EDA section looks nice and it effectively communicates the question to answer but if we want to show it more effectively I would recommend doing a correlation matrix to better illustrate the correlation relationship.")("To enhance its effectiveness, please consider incorporating a correlation matrix. )
[`feedback1`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1839314479)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/129)
- Added more references
[`feedback2`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840038049)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/b8cc5d1745e80ecc9ab6e2c74301c0d5314a1bf7)
[`pull request`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/127)
- community contribution guidelines [`pull request`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/125)
- Saved another pickle object from model_selection.py [`pull request`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/132)

### Fixed

- Typo in command line that was causing error for optimization.py
[`feedback1`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1839314479)
[`feedback2`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840038049)
[`feedback3`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840092852)
[`feedback4`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1841780569)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/1aac98a1cc153af4e1144b0d87ef405bf7610f5f)

- Fixed optimization.py to use selected model pickle for hyperparamter optimization.
[`feedback3`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840092852)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/8c76480a6ba5d5fffce3c0c2bc41d25323f06186)

- Fixed typo and Dockerfile dependency in README
[`feedback2`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840038049)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/a2b861a09a04eebf6f5d57d8cccf5949ed32323d)

### Changed

- Dockerfile and pushed the latest version image with 'make' dependency
[`Action`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/actions/runs/7123258670)
- docker-compose.yml file with updated image tag
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/b9c55b91f5957015a6238eb9c8cbb23b8d6ef92d)
- Histogram in EDA (encoded color to target class)
[`feedback3`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840092852)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/4cd78ce111e2f7bc156b3f0bc641e6495a45874c)
- Added more changes in CHANGELOG.md [`pull request`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/134)
- RADEME.md Usage part to replace all the command lines with make clean and make all
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/5e251ebabadf67bd8fc8efcac937717e519d4fa0)
[`commit`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/commit/fa64537df91b329e856b60540d6270a61cee8a7e)

### Removed

- Funtion (optimization.py in scr) that is not in use [`feedback2`](https://github.com/UBC-MDS/data-analysis-review-2023/issues/4#issuecomment-1840038049) [`pull request`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/135)
- command_line_prompt.md [`pull request`](https://github.com/UBC-MDS/dsci_522_group_8_bank_marketing_project/pull/139)


