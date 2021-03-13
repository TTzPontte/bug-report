class GetAll(event, context):
    def handler(self):
        return {
            "staus": 200
        }


def handler(event, context):
    GetAll(event, context).run()
