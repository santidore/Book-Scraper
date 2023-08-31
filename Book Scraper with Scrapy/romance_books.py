import scrapy

class RomanceBooksSpider(scrapy.Spider):
    name = 'romance_books_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/category/books/romance_8/index.html']

    def parse(self, response):
        #Iteramos sobre cada artículo que contiene información de un libro
        for book in response.xpath('//article[@class="product_pod"]'):
            #Extraemos el título del libro
            title = book.xpath('h3/a/@title').get()
            
            #Extraemos el precio del libro y lo convertimos a un número decimal
            price = book.xpath('div[@class="product_price"]/p[@class="price_color"]/text()').re_first(r'£(\d+\.\d+)')
            price = float(price)
            
            #Utilizamos XPath relativo para obtener el contenido completo de la etiqueta <p> que contiene "In stock" y <i>
            availability_text = ''.join(book.xpath('.//p[contains(@class, "availability")]/node()').extract()).strip()
            
            #Verificamos si el campo de disponibilidad del stock contiene "In stock" y establecemos el valor de disponibilidad en consecuencia
            if "In stock" in availability_text:
                availability = True
            else:
                availability = False
            
            #Extraemos la URL de la imagen de portada del libro y la convertimos en una URL absoluta
            imageUrl = book.xpath('div[@class="image_container"]/a/img[@class="thumbnail"]/@src').get()
            imageUrl = response.urljoin(imageUrl)

            #Devolvemos un diccionario con la información del libro
            yield {
                'title': title,
                'price': price,
                'stock': availability,
                'imageUrl': imageUrl,
            }

        #Verificamos si hay una página siguiente y continuamos la extracción si es el caso
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)



