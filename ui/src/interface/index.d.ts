interface Drone {
    id: number;
    name: string;
}

interface Task {
    description: string;
    drones: Drone[];
    id: number;
    is_executed: boolean;
    name: string;
}
