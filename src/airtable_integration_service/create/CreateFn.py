def handler(event, context):
    report = event.get('report')
    report_table.create(report)

    return { 'statusCode': 200 }
