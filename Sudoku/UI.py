import pygame as py

class UI:

    BLACK = (0 ,0 ,0)
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    (WIDTH, HEIGHT) = (400, 400)
    screen = None 

    def __init__(self):

        py.init()

        self.screen = py.display.set_mode((self.WIDTH, self.HEIGHT))
        py.display.set_caption('I LOVE U BABY')
        self.screen.fill(self.WHITE)

        self.drawGrid()


    def drawGrid(self):

        cols = [self.WIDTH/3, self.WIDTH/3 * 2]
        rows = [self.HEIGHT/3, self.HEIGHT/3 * 2]


    

        py.draw.line(self.screen, self.GREY, (cols[0]/3, 0), (cols[0]/3, self.HEIGHT) ,2)
        py.draw.line(self.screen, self.GREY, (cols[0]/3 * 2, 0), (cols[0]/3 * 2, self.HEIGHT) ,2)
        py.draw.line(self.screen, self.GREY, (cols[1]/3 * 2, 0), (cols[1]/3 * 2, self.HEIGHT) ,2)
        py.draw.line(self.screen, self.GREY, (cols[1]/3 * 2.5 , 0), (cols[1]/3 * 2.5, self.HEIGHT) ,2)
        py.draw.line(self.screen, self.GREY, (cols[1]/3 * 4, 0), (cols[1]/3 * 4, self.HEIGHT) ,2)
        py.draw.line(self.screen, self.GREY, (cols[1]/3 * 3.5 , 0), (cols[1]/3 * 3.5, self.HEIGHT) ,2)

   
        py.draw.line(self.screen, self.GREY, (0, rows[0]/3), (self.WIDTH, rows[0]/3) ,2)
        py.draw.line(self.screen, self.GREY, (0, rows[0]/3 * 2), (self.WIDTH, rows[0]/3 * 2) ,2)
        py.draw.line(self.screen, self.GREY, (0, rows[1]/3 * 2), (self.WIDTH, rows[1]/3 * 2) ,2)
        py.draw.line(self.screen, self.GREY, (0, rows[1]/3 * 2.5), (self.WIDTH, rows[1]/3 * 2.5) ,2)
        py.draw.line(self.screen, self.GREY, (0, rows[1]/3 * 4), (self.WIDTH, rows[1]/3 * 4) ,2)
        py.draw.line(self.screen, self.GREY, (0, rows[1]/3 * 3.5), (self.WIDTH, rows[1]/3 * 3.5) ,2)

        py.draw.line(self.screen, self.BLACK, (cols[1], 0), (cols[1], self.HEIGHT) ,3)
        py.draw.line(self.screen, self.BLACK, (cols[0], 0), (cols[0], self.HEIGHT) ,3)

        py.draw.line(self.screen, self.BLACK, (0, rows[0]), (self.WIDTH, rows[0]) ,3)
        py.draw.line(self.screen, self.BLACK, (0 , rows[1]), (self.WIDTH ,rows[1]) ,3)

    def drawBoard(self, values):

        py.time.delay(500)

        self.screen.fill(self.WHITE)
        self.drawGrid()

        countx = 0 
        county = 0
        for x in values:

            font = py.font.SysFont('arial', int(20/len(values[x])))

            text = font.render(values[x], True , self.BLACK)
            self.screen.blit(text, (countx * 45 + 16, county * 45 + 10))
            countx += 1
            if countx > 8:
                countx = 0
                county += 1
        py.display.update()



