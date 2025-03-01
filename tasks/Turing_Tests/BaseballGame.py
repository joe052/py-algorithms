class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        data = []
        for i in ops:
            try:
                data.append(int(i))
            except:
                if i == "+":
                    data.append(data[len(data) - 1] + data[len(data) - 2])
                elif i == "D":
                    data.append(data[len(data) - 1] * 2)
                elif i == "C":
                    data.pop()
        return sum(data)
