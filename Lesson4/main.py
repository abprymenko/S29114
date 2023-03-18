import Student as s
import Human as h
bogdan = s.Student("Bogdan", 14, 190, 10,11, "HTML")
bogdan.showInfo()

human = h.Human("Human default", 10, 150)
human.__showInfoHuman__()

bogdan.Move()