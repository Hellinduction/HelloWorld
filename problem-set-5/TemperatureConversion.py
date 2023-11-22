# For converting between Celsius and Fahrenheit
import Utils


def convertCtoF(c):
    f = round(c * 9 / 5 + 32, 2)
    return "Temperature in C: ", f"Temperature in F: {f}"


def convertFtoC(f):
    c = round((f - 32) * 5 / 9, 2)
    return "Temperature in F: ", f"Temperature in C: {c}"


OPTIONS = {
    "c to f": convertCtoF,
    "f to c": convertFtoC
}


def check_float(detail):
    try:
        float(detail)
        return True
    except:
        return False


def check_option(detail):
    return detail is not None and detail.lower() in OPTIONS.keys()


def getDetail(question, predicate, error):
    while True:
        fail_reason = None

        try:
            detail = input(question)

            if predicate is not None and not predicate(detail):
                fail_reason = error
        except:
            fail_reason = error

        if fail_reason is not None:
            print(fail_reason)
            continue

        break

    return detail


def start():
    conversion = getDetail("Conversion: ", check_option, f"Invalid option. Valid options: {Utils.formatStrList(OPTIONS.keys())}").lower()
    method = OPTIONS.get(conversion)

    temperature = float(getDetail(method(0)[0], check_float, "Invalid temperature."))
    calculated_temperature = method(temperature)

    print(calculated_temperature[1])


if __name__ == "__main__":
    start()
