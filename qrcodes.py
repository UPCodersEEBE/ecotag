
import segno
qr = segno.make('The Beatles -- Let It Be', error='h')
qr.to_artistic(background='yellowc.jpg', target='letitbe.jpg', scale=20)