from mrjob.job import MRJob

"""
    Use MRWordCount that inherits MRJob methods: map, combine, reduce
"""
class MRWordCount(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield(word, 1)

    def reducer(self, word, counts):
        yield(word, sum(counts))

if __name__ == '__main__':
    MRWordCount.run()