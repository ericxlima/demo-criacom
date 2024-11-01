'use client'

import { useRef } from "react"
import { Carousel, CarouselContent, CarouselItem } from "@/components/ui/carousel"
import { Badge } from "@/components/ui/badge"
import Autoplay from "embla-carousel-autoplay"

export default function Home() {
  const plugin = useRef(
    Autoplay({ delay: 3000, stopOnInteraction: false })
  )

  const articles = [
    {
      id: 1,
      title: "Board Review: John John Florence and Jon Pyzel",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "GALLERY",
      date: "Yesterday",
    },
    {
      id: 2,
      title: "Ultimate Guide to Understanding Neoprene",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "NEWS",
      date: "Yesterday",
    },
    {
      id: 3,
      title: "How to Choose Your Perfect Board",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "NEWS",
      date: "Yesterday",
    },
    {
      id: 4,
      title: "How to Choose Your Perfect Board",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "NEWS",
      date: "Yesterday",
    },
    {
      id: 5,
      title: "How to Choose Your Perfect Board",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "NEWS",
      date: "Yesterday",
    },
    {
      id: 6,
      title: "How to Choose Your Perfect Board",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "NEWS",
      date: "Yesterday",
    },
    {
      id: 7,
      title: "How to Choose Your Perfect Board",
      image: "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png",
      category: "NEWS",
      date: "Yesterday",
    },
  ]

  return (
    <div className="w-full bg-[#1a3947] min-h-screen flex items-center">
      <Carousel
        opts={{
          align: "start",
          loop: true,
        }}
        plugins={[plugin.current]}
        className="w-full pl-8"
      >
        <CarouselContent className="-ml-2 md:-ml-4">
          {articles.map((article) => (
            <CarouselItem key={article.id} className="pl-2 md:pl-4 md:basis-1/2 lg:basis-1/3">
              <div className={`relative aspect-[4/5] overflow-hidden rounded-lg group bg-no-repeat bg-cover
                bg-[url(https://t3.ftcdn.net/jpg/05/85/86/44/360_F_585864419_kgIYUcDQ0yiLOCo1aRjeu7kRxndcoitz.jpg)]`}>
                <div className="absolute inset-0 bg-gradient-to-b from-black/0 via-black/20 to-black/90" />
                <div className="absolute top-4 left-4">
                  <Badge className="bg-orange-500 hover:bg-orange-600">{article.category}</Badge>
                </div>
                <div className="absolute inset-x-4 bottom-4 flex flex-col gap-2">
                  <h3 className="text-xl md:text-2xl font-bold text-white leading-tight">
                    {article.title}
                  </h3>
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-gray-300">{article.date}</span>
                  </div>
                </div>
              </div>
            </CarouselItem>
          ))}
        </CarouselContent>
      </Carousel>
    </div>
  )
}