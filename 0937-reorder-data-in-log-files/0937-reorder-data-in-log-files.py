class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            splitted_log = log.split()
            if splitted_log[1].isalpha():
                letter_logs.append(splitted_log)
            else:
                digit_logs.append(log)

        letter_logs = sorted(letter_logs, key=lambda x: (x[1:], x[0]))
        letter_logs = [" ".join(log) for log in letter_logs]

        return letter_logs + digit_logs
