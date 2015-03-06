import codecs
unistr = u'\u0660\u2000ab ...'
(UTF8_encode, UTF8_decode,
UTF8_streamreader, UTF8_streamwriter) = codecs.lookup('UTF-8')

output = UTF8_streamwriter( open( '/tmp/output', 'wb' ))
output.write( unistr )
output.close()

input = UTF8_streamreader( open( '/tmp/output', 'rb' ))
print repr(input.read())
input.close()
