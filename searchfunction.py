from PageObject.TableSorting import TableSearchPage


def test_table_search(driver):
    page = TableSearchPage(driver)
    page.load()
    page.search("New York")

    assert page.get_visible_rows_count() == 5, "Expected 5 results, but found different count."
    print("Test passed: 5 entries displayed correctly for 'New York'.")










