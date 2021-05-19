db.users.drop();
db.users.insertMany([
    {
        _id: 1,
        email: 'foo.bar@email.com',
        name: "foo.bar",
        password: 'lol password ez',
        birthday: "1970/01/01",
        gender: "Male",
        weight: '80kg',
        height: '1.75m',
        hair_colour: 'black',
        eye_colour: 'blue',
        sexual_orientation: "Heterosexual",
        education: "University",
        smoker: false,
        drinker: false,
        children: false,
        status: "Student",
        bio: "bla bla bla bla bla bla bla bla bla bla",
        pfp: "path",
        photos: "path",
        type: "premium"
    }
]);