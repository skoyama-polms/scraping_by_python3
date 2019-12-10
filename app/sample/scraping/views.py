import urllib3, certifi, csv, urllib, datetime

from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'scraping/index.html', context)


def do_scraping(request):
    target_url = request.POST['target_url']
    target_tag = request.POST['target_tag']
    target_attribute = request.POST['target_attribute']

    # httpsの証明書検証を実行している
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    tags = http.request('GET', target_url)

    soup = BeautifulSoup(tags.data, 'html.parser')

    results = {}
    for i, tag in enumerate(soup.find_all(target_tag)):
        results[i] = {
            "target_url": target_url,
            "target_tag": target_tag,
            "target_attribute": target_attribute,
            "result_value": tag.get(target_attribute),
        }

    now = datetime.datetime.now()

    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote(('scraping_results_' + now.strftime('%Y%m%d%H%M%S_%f') + '.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)

    writer = csv.writer(response)

    for i in range(len(results)):
        writer.writerow([
            results[i]["target_url"],
            results[i]["target_tag"],
            results[i]["target_attribute"],
            results[i]["result_value"],
        ])

    return response
