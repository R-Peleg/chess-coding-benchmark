# chess-coding-benchmark
benchmark for assessing coding capabilities in chess-related tasks

## Structure
 * games - Contain games used for testing
 * questions - The coding questions
 * scripts - The scripts to run the tests

## How to run
for a quick example, run the following command:
```bash
python scripts/check_solution.py questions/traveling_rook llm_answers/claude_moving_rooks_oneshot.py
```

You should see the result:
```
Success: games/moving_rooks1.pgn
Success: games/fast_castling_both_sides.pgn
Success: games/moving_rooks_promotion.pgn
```
