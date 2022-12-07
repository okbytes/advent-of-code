const data = await Deno.readTextFile("input.txt")
const example = await Deno.readTextFile("example.txt")

// --- part 1
// example answer: 15
// answer: 15572

const scores = {
	A: 1, // rock
	X: 1,
	B: 2, // paper
	Y: 2,
	C: 3, // scissors
	Z: 3,
} as const
const lose = 0,
	win = 6,
	draw = 3

const items = data.split("\n")

const totalPart1 = items.reduce((acc, v) => {
	const [opKey, meKey] = v.split(" ") as [keyof typeof scores, keyof typeof scores]

	const me = scores[meKey] as number
	const op = scores[opKey] as number

	// scissors vs rock
	if (op === 3 && me === 1) {
		// win
		return acc + win + scores[meKey]
	}
	// rock vs scissors
	if (op === 1 && me === 3) {
		// lose
		return acc + lose + scores[meKey]
	}

	if (me > op) {
		return acc + win + me
	}
	if (me === op) {
		return acc + draw + me
	}
	return acc + lose + me
}, 0)

// console.log(totalPart1)

// --- part 2
// example answer: 12
// answer: 16098

const items2 = data.split("\n")

const totalPart2 = items2.reduce((acc, v) => {
	const [opMove, meResult] = v.split(" ") as [keyof typeof scores, keyof typeof scores]

	const op = scores[opMove] as number

	switch (meResult) {
		// lose
		case "X": {
			return acc + lose + (op === 1 ? 3 : op - 1)
		}
		// draw
		case "Y": {
			return acc + draw + op
		}
		// win
		case "Z": {
			return acc + win + (op === 3 ? 1 : op + 1)
		}
	}
	return acc
}, 0)

console.log(totalPart2)
