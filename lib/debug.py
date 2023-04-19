from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Attraction, City, Hotel, Restaurant


if __name__ == '__main__':

    engine = create_engine('sqlite:///test.db')
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(City).delete()
    session.query(Attraction).delete()

    nyc = City(name='New York', state='NY', country='USA')
    la = City(name='Los Angeles', state='CA', country='USA')
    sf= City(name='San Francisco', state='CA', country='USA')
    chs = City(name='Charleston', state = 'SC', country='USA')
    lv = City(name='Las Vegas', state = 'NV', country='USA')
    session.add_all([nyc, la, sf, chs, lv])
    session.commit()


    ritz = Hotel(name='Ritz', city_id=1)            #NY
    plaza = Hotel(name='The Plaza', city_id=1)      #NY
    regis = Hotel(name='The St. Regis', city_id=1)  #NY
    hilton = Hotel(name='Hilton', city_id=2)        #LA
    hyatt = Hotel(name='Hyatt', city_id=2)          #LA
    conrad = Hotel(name='Conrad', city_id=2)        #LA
    marriott = Hotel(name='Marriott', city_id=3)    #SF
    sheraton = Hotel(name='Sheraton', city_id=3)    #SF
    fairmont = Hotel(name='Fairmont', city_id=3)    #SF
    belmond = Hotel(name='Belmond', city_id=4)      #Charles
    tides = Hotel(name='Tides', city_id=4)          #Charles
    wentworth = Hotel(name= 'The Wentworth', city_id=4) #Charles
    mgm = Hotel(name= 'MGM Grand', city_id=5)        #Vegas
    wynn = Hotel(name= 'Wynn', city_id=5)            #Vegas
    veniant = Hotel(name= 'The Veniant', city_id=5)  #Vegas
    session.add_all([ritz, plaza, regis, hilton, hyatt,conrad, marriott, sheraton,fairmont, belmond, tides,wentworth, mgm, wynn,veniant])
    session.commit()

    # Restaurants
    # New York
    ben_and_jacks_steakhouse = Restaurant(name='Ben & Jacks Steakhouse', city_id=1)
    la_grande_boucherie = Restaurant(name='La Grande Boucherie', city_id=1)
    numero_28_pizzeria = Restaurant(name='Numero 28 Pizzeria', city_id=1)
    bagels_and_schmear = Restaurant(name='Bagels & Schmear', city_id=1)
    # Los Angeles
    perch = Restaurant(name='Perch', city_id=2)
    amor = Restaurant(name='Amor y Tacos', city_id=2)
    lazy_dog = Restaurant(name='Lazy Dog', city_id=2)
    geezers = Restaurant(name='Geezers', city_id=2)
    # San Francisco
    zazie = Restaurant(name='Zazie', city_id=3)
    spruce = Restaurant(name='Spruce', city_id=3)
    rich_table = Restaurant(name='Rich Table', city_id=3)
    hillstone = Restaurant(name='Hillstone', city_id=3)
    # Charleston
    fig = Restaurant(name='FIG', city_id=4)
    charleston_grill = Restaurant(name='Charleston Grill', city_id=4)
    stellas = Restaurant(name='Stellas', city_id=4)
    husk = Restaurant(name='Husk', city_id=4)
    # Las Vegas
    black_tap = Restaurant(name='Black Tap', city_id=5)
    honey_salt = Restaurant(name='Honey Salt', city_id=5)
    gritz = Restaurant(name='Gritz Cafe', city_id=5)
    flower_child = Restaurant(name='Flower Child', city_id=5)
    session.query(Restaurant).filter(Restaurant.name.in_(['Ben & Jacks Steakhouse', 'La Grande Boucherie', 'Numero 28 Pizzeria','Bagels & Schmear', 'Perch', 'Amor y Tacos', 'Lazy Dog', 'Geezers', 'Zazie', 'Spruce', 'Rich Table', 'Hillstone', 'FIG', 'Charleston Grill', 'Stellas', 'Husk', 'Black Tap', 'Honey Salt', 'Gritz Cafe', 'Flower Child'])).all()
    session.commit()


    es = Attraction(name='Empire State Building', city_id=1)
    sl = Attraction(name='Statue of Liberty', city_id=1)
    cp = Attraction(name='Central Park', city_id=1)
    hs = Attraction(name='Hollywood Sign', city_id=2)
    hwf = Attraction(name='Hollywood Walk of Fame', city_id=2)
    vb = Attraction(name='Venice Beach', city_id=2)
    ggb = Attraction(name='Golden Gate Bridge', city_id=3)
    ai = Attraction(name='Alcatraz Island', city_id=3)
    op = Attraction(name='Oracle Park', city_id=3)
    ao = Attraction(name='Angel Oak Tree', city_id=4)
    fb = Attraction(name='Folly Beach', city_id=4)
    mp = Attraction(name='Magnolia Plantation', city_id=4)
    fs = Attraction(name='Fremont Street', city_id=5)
    bf = Attraction(name='Bellagio Fountain', city_id=5)
    lvs = Attraction(name='Las Vegas Strip', city_id=5)

    session.add_all([es, sl, cp, hs, hwf, vb, ggb, ai, op, ao, fb, mp, fs, bf, lvs])
    session.commit()