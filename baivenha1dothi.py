def greedy_coloring(graph):
    colors = {}  # Dictionary để lưu trữ màu của mỗi đỉnh
    color_count = 0  # Biến đếm số màu đã sử dụng

    # Sắp xếp các đỉnh theo số lượng đỉnh kề giảm dần
    sorted_vertices = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)

    for vertex in sorted_vertices:
        neighbor_colors = set()  # Tập hợp các màu đã sử dụng bởi các đỉnh kề
        for neighbor in graph[vertex]:
            if neighbor in colors:
                neighbor_colors.add(colors[neighbor])

        # Tìm màu có sẵn mà chưa được sử dụng bởi các đỉnh kề
        for color in range(color_count):
            if color not in neighbor_colors:
                colors[vertex] = color
                break
        else:
            colors[vertex] = color_count  # Nếu không có màu nào có sẵn, sử dụng màu mới
            color_count += 1

    return colors

# Đồ thị mới dưới dạng danh sách kề
graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E", "C"],
    "C": ["A", "B", "D", "E", "F"],
    "D": ["A", "C", "F", "G"],
    "E": ["B", "C", "F", "Z"],
    "F": ["C", "D", "E", "Z", "G"],
    "G": ["D", "F", "Z"],
    "Z": ["E", "F", "G"]
}

coloring = greedy_coloring(graph)



for vertex, color in coloring.items():
    print(f"Đỉnh {vertex} tô màu {color}")
