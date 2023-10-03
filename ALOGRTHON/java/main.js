var student = [
    {
        'id': 1,
        'name': 'leak',
        'age': 24
    },
    {
        'id': 2,
        'name': 'pov',
        'age': 45
    },
    {
        'id': 3,
        'name': 'kolab',
        'age': 5
    }
]

for (let value in student) {
    console.log(student[value]['id']);
    console.log(student[value]['name']);
    console.log(student[value]['age'])
}


for ( let i = 0; i < student.length; i++){
    console.log(student[i]['id']);
    console.log(student[i]['name']);
    console.log(student[i]['age'])
}

let i = 0;
while (i < student.length ){
    console.table(student[i].id);
    console.table(student[i].name);
    console.table(student[i].age)
    i ++;
}

student.forEach((item) => {
    console.log(item.name)
})










// var student = ['A', 'B', 'C'];
// console.log(student.length)
// for (let i = 0; i < student.length; i++) {
//     console.log(student[i])
// }

