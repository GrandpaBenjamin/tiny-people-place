class World {
    constructor(name,startingPopulation) {
        this.name = name;
        this.startingPopulation = startingPopulation;
    }

    tick(){
        print("tick")
    }
}

module.exports = World;