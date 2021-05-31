# Simplify the data

when I create a new dataframe with the json data the frame has a bunch of
extra variables that I don't need some examples are:
    1. puuid
    2. name
    3. accountId
and many other personal identifiers. It is safe to drop these and honestly might
be a bit more effecient if I go through and permanently delete them from the
json files themselves.


## Normalize the data

After I have dropped all of the 'useless' data I can go ahead and normalize
the data, this essentialy flattens the data into a simpler object to handle.
One problem with this technique though is that it is very time consuming. If I can
find an easier way to handle this operation it would be very benefitial. So far I have 
only `normalized` the `info['participants']` because this holds all of the data that I am looking for.

## Organize the data

// need to talk about organizing champions into numeric values
// as well as the role that somebody was



