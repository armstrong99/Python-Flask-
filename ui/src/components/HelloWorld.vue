<template>
  <div>
    <button @click="fetchDrones">Fetch Drones</button>
    <ul v-if="showDronesResult">
      <li v-for="(drone, index) in dronesResult" :key="index">
        {{ drone.name }} - {{ drone.id }} <!-- Adjust this based on your drone data structure -->
      </li>
    </ul>

    <button @click="fetchTasks">Fetch Tasks</button>
        <div v-if="showTasksResult" class="task-details">
          <h2>{{ tasksResult.name }}</h2>
          <p>{{ tasksResult.description }}</p>
          <div v-if="tasksResult.is_executed" class="executed">Executed</div>
          <div v-else class="not-executed">Not Executed</div>

          <h3>Drones:</h3>
          <ul>
            <li v-for="drone in tasksResult!.drones" :key="drone.id">{{ drone.name }}</li>
          </ul>
      </div>

    <button @click="executeTask">Execute Task</button>
    <p v-if="showExecuteTaskResult">{{ executeTaskResult }}</p>

    <button @click="fetchImages">Fetch Images</button>
    <p v-if="showImagesResult">{{ imagesResult }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const apiUrl = import.meta.env.VITE_API_ENDPOINT

const showDronesResult = ref(false)
const showTasksResult = ref(false)
const showExecuteTaskResult = ref(false)
const showImagesResult = ref(false)

const dronesResult = ref<Array<{name: string, id: number}>>([])
const tasksResult = ref<Task>({description: '', name: '', id:0, is_executed: false, drones: [{id: 0, name: ''}]})
const executeTaskResult = ref('')
const imagesResult = ref('')

const fetchDrones = async () => {
  try {
    console.log(apiUrl)
    dronesResult.value = []
    showDronesResult.value = true
    const result = await fetch(apiUrl+'/drones', {mode: "cors"})
    const data = await result.json()
    dronesResult.value = data
  } catch (error) {
    console.error('Error fetching drones:', error)
  }
}

const fetchTasks = async () => {
  try {
    showTasksResult.value = false
    const response = await fetch(apiUrl+'/tasks/1')
    const data = await response.json()
    showTasksResult.value = true
    tasksResult.value = (data)
  } catch (error) {
    console.error('Error fetching tasks:', error)
  }
}

const executeTask = async () => {
  try {
    showExecuteTaskResult.value = true
    const taskId = 1 // Replace with actual task ID
    const response = await fetch(apiUrl+`/tasks/${taskId}/execute`, { method: 'POST' })
    const data = await response.json()
    executeTaskResult.value = JSON.stringify(data)
  } catch (error) {
    console.error('Error executing task:', error)
  }
}

const fetchImages = async () => {
  try {
    showImagesResult.value = true
    const taskId = 1 // Replace with actual task ID
    const response = await fetch(apiUrl+`/tasks/${taskId}/images`)
    const data = await response.json()
    imagesResult.value = JSON.stringify(data)
  } catch (error) {
    console.error('Error fetching images:', error)
  }
}
</script>
