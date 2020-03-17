import os


def test_runner(path: str):
    result = []
    for file in os.listdir(path):

        if '.a' not in file:
            test_data = open(path + '/' + file, "r")
            answer_data = open(path + '/' + file + '.a', "r")
            args = [line.rstrip('\n') for line in test_data]
            answer = [line.rstrip('\n') for line in answer_data]
            result.append((args, answer, file))
            test_data.close()
            answer_data.close()
    return result
