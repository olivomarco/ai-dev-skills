const optionIndex = process.argv.indexOf("--format");
const format = optionIndex === -1 ? "json" : process.argv[optionIndex + 1];
if (!["json", "csv"].includes(format)) {
  console.error("Expected --format json or --format csv");
  process.exit(2);
}
console.log(format);
