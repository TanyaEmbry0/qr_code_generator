import pyqrcode
from code import my_link



def my_qr(format_qr, link_qr):
    my_link = input('l:')
    my_img = pyqrcode.create(my_link)


def my_format(f):
    my_format = input('f:')

    my_img = pyqrcode.create(my_link)
    if my_format == 'png':
        my_img.png('my_img.png', scale=8)
    elif my_format == 'svg':
        my_img.svg('my_img.svg', scale=6)
    elif my_format == 'jpg':
        my_img.save('my_img.jpg')
    else:
        print('Input is NOT correct!')
        quit()


my_qr(my_format(), my_link)




