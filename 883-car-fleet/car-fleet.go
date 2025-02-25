func carFleet(target int, position []int, speed []int) int {
    type Car struct {
	position int
	speed    int
    }
    n := len(position)
	cars := make([]Car, n)
	for i := 0; i < n; i++ {
		cars[i] = Car{position[i], speed[i]}
	}

	sort.Slice(cars, func(i, j int) bool {
		return cars[i].position > cars[j].position
	})

	stack := []float64{}
	for _, car := range cars {
		time := float64(target-car.position) / float64(car.speed)
		stack = append(stack, time)
		if len(stack) >= 2 && stack[len(stack)-1] <= stack[len(stack)-2] {
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack)
}