import re
data = """
615-555-7164
800-555-5669
560-555-5153
900-555-9340
714-555-7405
800-555-6771"""

pattern = r"\b\d{3}-\d{3}-\d{4}\b"
phones = re.findall(pattern, data)


def mask_phone_number(ph):
    if '-' in ph:
        part1,part2,part3 = ph.split('-')
        masked_phone = f"###-###-{part3}"
    return masked_phone

masked_phones = [mask_phone_number(e) for e in phones]
print(masked_phones)





"""
Data:
['615-555-7164', '800-555-5669', '560-555-5153',
 '900-555-9340', '714-555-7405', '800-555-6771']
Output
['###-###-164', '###-###-669', '###-###-153',
 '###-###-340', '###-###-405', '###-###-771']

"""