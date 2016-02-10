import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = int(x)
        result = []
        text = ''
        negative = False
        answer = ''

        if start < 0:
        	start = start * -1
        	negative = True

        text = str(start)

        for i in text:
        	result.insert(0,i)

        for i in result:
        	answer = answer + str(i)

        try:
        	answer = int(answer)
        except ValueError:
        	print('Error ' + answer)

        if answer > (2 ** 31 - 1):
            return(0)

        if negative:
        	answer = answer * -1

        return(answer)
