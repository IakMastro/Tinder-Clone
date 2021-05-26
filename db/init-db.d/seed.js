db.users.drop();
db.users.insertMany([
    {
        _id: 'da3916f299434734b3ac4014a13d231e',
        email: 'foo@email.com',
        username: "foo",
        name: "foo",
        surname: "bar",
        password: 'bar',
        birthday: "1970-01-01",
        gender: "Male",
        weight: '80',
        height: '1.75',
        hair_colour: 'black',
        eye_colour: 'blue',
        sexual_orientation: "Heterosexual",
        education: "University",
        smoker: false,
        drinker: false,
        children: false,
        status: "Student",
        bio: "bio here",
        pfp: "path",
        photos: "path",
        type: "premium"
    }
]);