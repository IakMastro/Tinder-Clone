export function calculate_age(birthday: Date): number {
    return Math.floor((Date.now() - birthday.getTime()) / 3.15576e+10)
}