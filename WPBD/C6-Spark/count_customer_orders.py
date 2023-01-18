from mrjob.job import MRJob
from mrjob.step import MRStep

class MRBillCompute(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper = self.map_by_value,
                reducer = self.reduce_by_customer
            )
        ]

    def map_by_value(self, _, line):
        for row in line.split():
            customer_id, product_id, value = row.split(",")
            yield (customer_id, float(value))

    def reduce_by_customer(self, customer_id, values):
        yield (round(sum(values), 2), customer_id)


if __name__ == '__main__':
    MRBillCompute.run()