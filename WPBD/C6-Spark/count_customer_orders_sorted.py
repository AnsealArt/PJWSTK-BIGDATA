from mrjob.job import MRJob
from mrjob.step import MRStep

class MRBillCompute(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper = self.map_by_value,
                reducer = self.reduce_by_customer
            ),
            MRStep(
                reducer = self.sort_by_value
            )
        ]

    def map_by_value(self, _, line):
        for row in line.split():
            customer_id, product_id, value = row.split(",")
            yield (customer_id, float(value))

    def reduce_by_customer(self, customer_id, values):
        yield None, (round(sum(values), 2), customer_id)

    def sort_by_value(self, customer_id, values):
        for value in sorted(values, reverse=True):
            yield (value)
        
            

if __name__ == '__main__':
    MRBillCompute.run()