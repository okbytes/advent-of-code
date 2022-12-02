const data = await Deno.readTextFile("input.txt")
const example = await Deno.readTextFile("example.txt")

// --- part 1
// example answer: 24000

const total = data.split(/\n\n/g).reduce((total, calories) => {
	const tempTotal = calories.split(/\n/g).reduce((acc, curVal) => {
		return acc + parseInt(curVal)
	}, 0)
	if (tempTotal > total) {
		return tempTotal
	}
	return total
}, 0)

console.log(total)

// --- part 2
// example answer: 45000

const individualTotals = data
	.split(/\n\n/g)
	.reduce((acc: number[], curVal) => {
		const curTotal = curVal.split(/\n/g).reduce((acc, curVal) => {
			return acc + parseInt(curVal)
		}, 0)
		acc.push(curTotal)
		return acc
	}, [])
	.sort((a, b) => b - a)

const top3Total = individualTotals.slice(0, 3).reduce((acc, curVal) => acc + curVal, 0)

console.log(top3Total)
