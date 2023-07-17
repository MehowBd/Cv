//
// Created by Michał Badura, AiR II, grupa 1a, nr 407049
//
#include "TSP.hpp"
#include <algorithm>
#include <stack>
#include <optional>

std::ostream& operator<<(std::ostream& os, const CostMatrix& cm) {
    for (std::size_t r = 0; r < cm.size(); r++) {
        for (std::size_t c = 0; c < cm.size(); c++) {
            const auto& elem = cm[r][c];
            os << (is_inf(elem) ? "INF" : std::to_string(elem)) << " ";
        }
        os << "\n";
    }
    os << std::endl;

    return os;
}

/* PART 1 */

/**
 * Create path from unsorted path and last 2x2 cost matrix.
 * @return The vector of consecutive vertex.
 */
path_t StageState::get_path() {
    std::size_t size = matrix_.size();
    unsorted_path_t uns_path = get_unsorted_path();
    for (std::size_t i = 0; i < size; i++){
        for (std::size_t j = 0; j < size; j++){
            if (matrix_[i][j] != INF){
                uns_path.push_back(vertex_t{i, j});
            }
        }
    }
    unsorted_path_t sor_path = {uns_path[0]};

    for (std::size_t sor_path_iter = 0; sor_path_iter < uns_path.size() - 1; sor_path_iter++){
        for (std::size_t i = 1; i < uns_path.size(); i++){
            vertex_t vertex = uns_path[i];
            if (vertex.row == sor_path[sor_path_iter].col){
                sor_path.push_back(vertex);
                break;
            }
        }
    }
    std::vector<std::size_t> final_path;
    for (const auto& vertex: sor_path){
        final_path.push_back(vertex.col + 1);
    }
    return final_path;
}

/**
 * Get minimum values from each row and returns them.
 * @return Vector of minimum values in row.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_rows() const {
    std::size_t size = matrix_.size();
    std::vector<cost_t> min_values(size);

    for(std::size_t i=0; i < size; i++) {
        min_values[i] = matrix_[i][0];
        for(std::size_t j=0; j < size; j++) {
            if(min_values[i] > matrix_[i][j]) {
                min_values[i] = matrix_[i][j];
            }
        }
    }
    return min_values;
}


/**
 * Reduce rows so that in each row at least one zero value is present.
 * @return Sum of values reduced in rows.
 */
cost_t CostMatrix::reduce_rows() {
    std::size_t size = matrix_.size();
    std::vector<cost_t> min = get_min_values_in_rows();
    cost_t reduced_sum = 0;

    for (std::size_t i = 0; i < size; i++) {
        for (std::size_t j = 0; j < size; j++) {
            if (matrix_[i][j] != INF) {
                matrix_[i][j] -= min[i];
            }
        }
        if (min[i] != INF) {
            reduced_sum += min[i];
        }
    }
    return reduced_sum;
}
/**
 * Get minimum values from each column and returns them.
 * @return Vector of minimum values in columns.
 */
std::vector<cost_t> CostMatrix::get_min_values_in_cols() const {
    std::size_t size = matrix_.size();
    std::vector<cost_t> min_values(size);

    for(std::size_t i=0; i < size; i++) {
        min_values[i] = matrix_[0][i];
        for(std::size_t j=0; j < size; j++) {
            if(min_values[i] > matrix_[j][i]) {
                min_values[i] = matrix_[j][i];
            }
        }
    }
    return min_values;
}

/**
 * Reduces rows so that in each column at least one zero value is present.
 * @return Sum of values reduced in columns.
 */
cost_t CostMatrix::reduce_cols() {
    std::size_t size = matrix_.size();
    std::vector<cost_t> m = get_min_values_in_cols();
    cost_t reduced_sum = 0;

    for (std::size_t i = 0; i < size; i++) {
        for (std::size_t j = 0; j < size; j++) {
            if (matrix_[j][i] != INF) {
                matrix_[j][i] -= m[i];
            }
        }
        if (m[i] != INF) {
            reduced_sum += m[i];
        }

    }
    return reduced_sum;
}

/**
 * Get the cost of not visiting the vertex_t (@see: get_new_vertex())
 * @param row
 * @param col
 * @return The sum of minimal values in row and col, excluding the intersection value.
 */
cost_t CostMatrix::get_vertex_cost(std::size_t row, std::size_t col) const {
    std::size_t size = matrix_.size();
    cost_t min_value_row = matrix_[row][0];
    cost_t min_value_col = matrix_[0][col];

    for(std::size_t index = 1; index < size; index++){
        if(index != col && matrix_[row][index] < min_value_row){
            min_value_row = matrix_[row][index];
        }
    }

    for(std::size_t index = 1; index < size; index++){
        if(index != row && matrix_[index][col] < min_value_col){
            min_value_col = matrix_[index][col];
        }
    }
    return min_value_col + min_value_row;
}

/* PART 2 */

/**
 * Choose next vertex to visit:
 * - Look for vertex_t (pair row and column) with value 0 in the current cost matrix.
 * - Get the vertex_t cost (calls get_vertex_cost()).
 * - Choose the vertex_t with maximum cost and returns it.
 * @param cm
 * @return The coordinates of the next vertex.
 */
NewVertex StageState::choose_new_vertex() {
    std::size_t size = matrix_.size();
    vertex_t new_vertex;
    cost_t vertex_cost = 0;
    cost_t possible_cost_new_vertex;

    for (std::size_t row_iteration = 0; row_iteration < size; row_iteration++){
        for (std::size_t col_iteration = 0; col_iteration < size; col_iteration++){
            if (matrix_[row_iteration][col_iteration] == 0){
                possible_cost_new_vertex = matrix_.get_vertex_cost(row_iteration, col_iteration);
                if (possible_cost_new_vertex > vertex_cost){
                    vertex_cost = possible_cost_new_vertex;
                    new_vertex.col = col_iteration;
                    new_vertex.row = row_iteration;
                }
            }
        }
    }
    return NewVertex(new_vertex, vertex_cost);
}

/**
 * Update the cost matrix with the new vertex.
 * @param new_vertex
 */
void StageState::update_cost_matrix(vertex_t new_vertex) {
    std::size_t size = matrix_.size();

    for (std::size_t index = 0; index < size; index++){
        matrix_[new_vertex.row][index] = INF;
        matrix_[index][new_vertex.col] = INF;
    }

    matrix_[new_vertex.col][new_vertex.row] = INF;

    unsorted_path_t uns_path;
    uns_path = unsorted_path_;

    for (std::size_t index = 0; index < unsorted_path_.size(); index++) {
        size = uns_path.size();
        for (std::size_t i = 0; i < size; i++) {
            for (std::size_t j = 0; j < size; j++) {
                if (uns_path[i].col == uns_path[j].row) {
                    matrix_[uns_path[j].col][uns_path[i].row] = INF;
                    uns_path.push_back({uns_path[i].row, uns_path[j].col});
                }
            }
        }
    }
}

/**
 * Reduce the cost matrix.
 * @return The sum of reduced values.
 */
cost_t StageState::reduce_cost_matrix(){
    cost_t reduced_values_rows = matrix_.reduce_rows();
    cost_t reduced_values_cols = 0;
    std::vector<cost_t> minimal_values = matrix_.get_min_values_in_cols();
    cost_t sum_values = 0;

    for (std::size_t i = 0; i < minimal_values.size() ; i++){
        sum_values += minimal_values[i];
    }

    if (sum_values != 0){
        reduced_values_cols = matrix_.reduce_cols();
    }
    return reduced_values_rows + reduced_values_cols;
}

/**
 * Given the optimal path, return the optimal cost.
 * @param optimal_path
 * @param m
 * @return Cost of the path.
 */
cost_t get_optimal_cost(const path_t& optimal_path, const cost_matrix_t& m) {
    cost_t cost = 0;

    for (std::size_t idx = 1; idx < optimal_path.size(); ++idx) {
        cost += m[optimal_path[idx - 1] - 1][optimal_path[idx] - 1];
    }

    // Add the cost of returning from the last city to the initial one.
    cost += m[optimal_path[optimal_path.size() - 1] - 1][optimal_path[0] - 1];

    return cost;
}

/**
 * Create the right branch matrix with the chosen vertex forbidden and the new lower bound.
 * @param m
 * @param v
 * @param lb
 * @return New branch.
 */
StageState create_right_branch_matrix(cost_matrix_t m, vertex_t v, cost_t lb) {
    CostMatrix cm(m);
    cm[v.row][v.col] = INF;
    return StageState(cm, {}, lb);
}

/**
 * Retain only optimal ones (from all possible ones).
 * @param solutions
 * @return Vector of optimal solutions.
 */
tsp_solutions_t filter_solutions(tsp_solutions_t solutions) {
    cost_t optimal_cost = INF;
    for (const auto& s : solutions) {
        optimal_cost = (s.lower_bound < optimal_cost) ? s.lower_bound : optimal_cost;
    }

    tsp_solutions_t optimal_solutions;
    std::copy_if(solutions.begin(), solutions.end(),
                 std::back_inserter(optimal_solutions),
                 [&optimal_cost](const tsp_solution_t& s) { return s.lower_bound == optimal_cost; }
    );

    return optimal_solutions;
}

/**
 * Solve the TSP.
 * @param cm The cost matrix.
 * @return A list of optimal solutions.
 */
tsp_solutions_t solve_tsp(const cost_matrix_t& cm) {

    StageState left_branch(cm);

    // The branch & bound tree.
    std::stack<StageState> tree_lifo;

    // The number of levels determines the number of steps before obtaining
    // a 2x2 matrix.
    std::size_t n_levels = cm.size() - 2;

    tree_lifo.push(left_branch);   // Use the first cost matrix as the root.

    cost_t best_lb = INF;
    tsp_solutions_t solutions;

    while (!tree_lifo.empty()) {

        left_branch = tree_lifo.top();
        tree_lifo.pop();

        while (left_branch.get_level() != n_levels && left_branch.get_lower_bound() <= best_lb) {
            // Repeat until a 2x2 matrix is obtained or the lower bound is too high...

            if (left_branch.get_level() == 0) {
                left_branch.reset_lower_bound();
            }

            // 1. Reduce the matrix in rows and columns.
            cost_t new_cost; // @TODO (KROK 1)
            new_cost = left_branch.reduce_cost_matrix();

            // 2. Update the lower bound and check the break condition.
            left_branch.update_lower_bound(new_cost);
            if (left_branch.get_lower_bound() > best_lb) {
                break;
            }

            // 3. Get new vertex and the cost of not choosing it.
            NewVertex new_vertex; // @TODO (KROK 2)
            new_vertex = left_branch.choose_new_vertex();


            // 4. @TODO Update the path - use append_to_path method.
            left_branch.append_to_path(new_vertex.coordinates);

            // 5. @TODO (KROK 3) Update the cost matrix of the left branch.
            left_branch.update_cost_matrix(new_vertex.coordinates);

            // 6. Update the right branch and push it to the LIFO.
            cost_t new_lower_bound = left_branch.get_lower_bound() + new_vertex.cost;
            tree_lifo.push(create_right_branch_matrix(cm, new_vertex.coordinates,
                                                      new_lower_bound));
        }

        if (left_branch.get_lower_bound() <= best_lb) {
            // If the new solution is at least as good as the previous one,
            // save its lower bound and its path.
            best_lb = left_branch.get_lower_bound();
            path_t new_path = left_branch.get_path();
            solutions.push_back({get_optimal_cost(new_path, cm), new_path});
        }
    }

    return filter_solutions(solutions); // Filter solutions to find only optimal ones.
}