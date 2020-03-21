import os


def test_runner(path: str):
    result = []
    for file in os.listdir(path):

        if '.a' not in file:
            test_data = open(path + '/' + file, "r")
            answer = None
            if os.path.exists(path + '/' + file + '.a'):
                answer_data = open(path + '/' + file + '.a', "r")
                answer = [line.rstrip('\n') for line in answer_data]
                answer_data.close()
            args = [line.rstrip('\n') for line in test_data]
            result.append((args, answer, file))
            test_data.close()

    return result
