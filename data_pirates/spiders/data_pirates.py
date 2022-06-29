from array import array
from typing import Optional
import scrapy

from data_pirates.items import DataPiratesLoader, DataPiratesItem

def striper(array_fields:list) -> list:

    list_objects = []
    for object in array_fields:

        if not object:
            list_objects.append('')
        else:
            list_objects.append(object.strip())

    return list_objects

class DataPirates(scrapy.Spider):

    name: Optional[str] = 'Correios'
    start_urls:list = ['https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm']


    def parse(self, response):

        for uf in response.xpath('//select[@class="f1col"]/option[not(contains(text(), "\r"))]//text()').getall():
            
            formdata = {'UF': uf,'rows': '100'}

            cb_kwargs = {'uf': uf}

            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                cb_kwargs=cb_kwargs,
                callback=self.parse_values
            )

    def parse_values(self, response, uf):
        last_row = response.xpath('//div[@class="ctrlcontent"]/text()').re(r"\r\xa0\xa01 a 100 de (\d*)")
        last_row = 1 if not last_row else int(last_row[0])//100 + 1

        for page in range(1, last_row+1):
            if page == 1:
                for row in response.xpath('//table[@class="tmptabela"][last()]//tr'):
                    items = DataPiratesLoader(DataPiratesItem())
                    array_fields = [uf,
                                    row.xpath('td[1]//text()').get(),
                                    row.xpath('td[2]//text()').get(),
                                    row.xpath('td[3]//text()').get(),
                                    row.xpath('td[4]//text()').get()
                                    ]

                    array_fields = striper(array_fields)
                    row_valid = True if len(list(filter(lambda x: x != '', array_fields))) > 1 else False
                    if row_valid:
                        items.add_fields(array_fields)
                        yield items.load_item()
            else:
                inicio = str(page*100 + 1)
                fim = str((page + 1)*100)
                formdata = {'uf': uf,
                            'pagini': inicio,
                            'pagfim': fim,
                            'rows': '100'
                            }

                cb_kwargs = {'uf': uf}

                yield scrapy.FormRequest.from_response(
                    response,
                    formdata=formdata,
                    cb_kwargs=cb_kwargs,
                    callback=self.parse_pagination
                )

    def parse_pagination(self, response, uf):
        for row in response.xpath('//table[@class="tmptabela"][last()]//tr'):
            items = DataPiratesLoader(DataPiratesItem())
            array_fields = [uf,
                            row.xpath('td[1]//text()').get(),
                            row.xpath('td[2]//text()').get(),
                            row.xpath('td[3]//text()').get(),
                            row.xpath('td[4]//text()').get()
                            ]
            array_fields = striper(array_fields)
            row_valid = True if len(list(filter(lambda x: x != '', array_fields))) > 1 else False
            if row_valid:
                items.add_fields(array_fields)
                yield items.load_item()