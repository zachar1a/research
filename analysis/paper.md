# final
Somethings to note, is that there is a possibility that
a player could have returned an item and purchased another
item.

Also, moving the items around determines what index they show up
in when the game complets, the data structure indexes them
from item[0-6]. If the match where to end and a player moved
their item5 to something more accessible such as key 2,
it would show up as their fifth item purchased being their second item.
This could potentially throw off the model that would be created using
items.
