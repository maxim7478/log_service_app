export function useDebounce(func: Function, delay: number) {
  let timeout = 0;
  return function(...args: any) {
    clearTimeout(timeout)
    timeout = setTimeout(() => func(...args), delay)
  }
}