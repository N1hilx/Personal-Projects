from enum import Enum, auto
from typing import Callable
from pathlib import Path
import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt


class Location(Enum):
    CITY = auto()
    NATURE = auto()


class PartOfDay(Enum):
    SUNRISESUNSET = auto()
    DAY = auto()
    NIGHT = auto()


class Season(Enum):
    SPRINGSUMMER = auto()
    AUTUMN = auto()
    WINTER = auto()


class Notes(Enum):
    NOTES = auto()
    NOT_NOTES = auto()


def classify_location(image: np.ndarray) -> Location:
    if image is None:
        return
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Na palety farieb v celom kode od labs.tineye.com a sluzby GPT3
    # som vyuzil analyzu farieb

    city_color_range = ((0, 0, 0), (100, 100, 100))        
    nature_color_range = ((30, 30, 30), (90, 255, 255))   

    city_mask = cv2.inRange(hsv_image, city_color_range[0], city_color_range[1])
    nature_mask = cv2.inRange(hsv_image, nature_color_range[0], nature_color_range[1])

    total_pixels = image.shape[0] * image.shape[1]
    city_percentage = cv2.countNonZero(city_mask) / total_pixels
    nature_percentage = cv2.countNonZero(nature_mask) / total_pixels

    if city_percentage > nature_percentage:
        return Location.CITY
    
    return Location.NATURE

def classify_time_of_day(image: np.ndarray) -> PartOfDay:
    if image is None:
        return
    
    hsv_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    day_color_range = ((50, 30, 30), (120, 255, 255))
    night_color_range =  ((0, 0, 0), (80, 80, 80))
    sunsetsunrise_color_range = ((0, 0, 40), (50, 255, 255))

    day_mask = cv2.inRange(hsv_image1, day_color_range[0], day_color_range[1])
    night_mask = cv2.inRange(hsv_image1, night_color_range[0], night_color_range[1])
    sunsetsunrise_mask = cv2.inRange(hsv_image1, sunsetsunrise_color_range[0], sunsetsunrise_color_range[1])

    total_pixels1 = image.shape[0]*image.shape[1]
    day_percentage = cv2.countNonZero(day_mask) / total_pixels1
    night_percentage = cv2.countNonZero(night_mask) / total_pixels1
    sunsetsunrise_percentage = cv2.countNonZero(sunsetsunrise_mask) / total_pixels1

    if day_percentage > night_percentage and day_percentage > sunsetsunrise_percentage:
        return PartOfDay.DAY
    elif night_percentage > day_percentage and night_percentage > sunsetsunrise_percentage:
        return PartOfDay.NIGHT
    
    return PartOfDay.SUNRISESUNSET


def classify_season(image: np.ndarray) -> Season:
    if image is None:
        return
    
    hsv_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    winter_color_range = ((90, 0, 0), (120, 255, 255))
    autumn_color_range = ((0, 20, 10), (120, 255, 190))
    springsummer_color_range = ((20, 30, 30), (120, 255, 255))

    winter_mask = cv2.inRange(hsv_image2, winter_color_range[0], winter_color_range[1])
    autumn_mask = cv2.inRange(hsv_image2, autumn_color_range[0], autumn_color_range[1])
    springsummer_mask = cv2.inRange(hsv_image2, springsummer_color_range[0], springsummer_color_range[1])

    total_pixels2 = image.shape[0]*image.shape[1]
    winter_percentage = cv2.countNonZero(winter_mask) / total_pixels2
    autumn_percentage = cv2.countNonZero(autumn_mask) / total_pixels2
    springsummer_percentage = cv2.countNonZero(springsummer_mask) / total_pixels2

    if winter_percentage > springsummer_percentage and winter_percentage > autumn_percentage:
        return Season.WINTER
    elif springsummer_percentage > winter_percentage and springsummer_percentage > autumn_percentage:
        return Season.SPRINGSUMMER
    
    return Season.AUTUMN


def classify_notes(image: np.ndarray) -> Notes:
    if image is None:
        return Notes.NOT_NOTES
    
    hsv_image3 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    writing_color_range = ((0, 0, 0), (180, 255, 50))
    paper_color_range = ((0, 0, 150), (180, 30, 255))

    writing_mask = cv2.inRange(hsv_image3, writing_color_range[0], writing_color_range[1])
    paper_mask = cv2.inRange(hsv_image3, paper_color_range[0], paper_color_range[1])

    total_pixels3 = image.shape[0] * image.shape[1]
    writing_percentage = cv2.countNonZero(writing_mask) / total_pixels3
    paper_percentage = cv2.countNonZero(paper_mask) / total_pixels3

    threshold = 0.6

    if writing_percentage + paper_percentage > threshold:
        return Notes.NOTES
    else:
        return Notes.NOT_NOTES



# ----------------------------------------------------
# --- Below this line is just code that runs tests ---
# ----------------------------------------------------

def test_category(path: str("/Users/zdeno/Desktop/kodiky/image_recognition/public_tests"), function: Callable[[np.ndarray], Enum], correct: Enum) -> bool:
    print(f"--- Testing {correct} classification! ---")
    correctly_classified = 0
    number_of_images = 0
    for image_path in Path(path).iterdir():
        image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        result = function(image)
        number_of_images += 1
        if result == correct:
            correctly_classified += 1
            print(f"[âœ“] Correctly classified {image_path}")
        else:
            print(f"[X] Incorrectly classified {image_path}, should be {correct}, your function returned {result}")
    print(f"Correctly classified {correctly_classified}/{number_of_images} for category {correct}")
    return correctly_classified == number_of_images

# Uprava kodu funkcie main bola ciastocne vykonana skrz ChatGPT,
# pretoze som nedokazal spustit testy
    
def main() -> None:
    base_path = "/Users/zdeno/Desktop/kodiky/image_recognition/public_tests"
    categories = {
        Location.NATURE: [f"{base_path}/nature", classify_location, False],
        Location.CITY: [f"{base_path}/city", classify_location, False],
        PartOfDay.SUNRISESUNSET: [f"{base_path}/sunrise_sunset", classify_time_of_day, False],
        PartOfDay.DAY: [f"{base_path}/midday", classify_time_of_day, False],
        PartOfDay.NIGHT: [f"{base_path}/night", classify_time_of_day, False],
        Season.SPRINGSUMMER: [f"{base_path}/spring_summer", classify_season, False],
        Season.AUTUMN: [f"{base_path}/autumn", classify_season, False],
        Season.WINTER: [f"{base_path}/winter", classify_season, False],
        Notes.NOTES: [f"{base_path}/notes", classify_notes, False],
        Notes.NOT_NOTES: [f"{base_path}/not_notes", classify_notes, False]
    }
    for category, info in categories.items():
        info[2] = test_category(info[0], info[1], category)

    all_correct = True
    for category, info in categories.items():
        if not info[2]:
            print(f"Test for {category} failed!")
            all_correct = False

    if all_correct:
        print("All test have passed!")
    else:
        print("Some test have failed!")


if __name__ == "__main__":
    main()
