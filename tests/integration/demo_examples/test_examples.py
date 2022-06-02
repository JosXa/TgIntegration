import pytest


pytestmark = pytest.mark.asyncio


async def test_dinopark_example(session_name):
    # Late import so that the autouse fixtures run first
    from examples.automation import dinoparkbot

    client = dinoparkbot.create_client(session_name)
    game = dinoparkbot.create_game_controller(client)
    await game.perform_full_run()


async def test_idletown_example(session_name):
    # Late import so that the autouse fixtures run first
    import examples.automation.idletown as idletown

    idletown.MAX_RUNS = 1
    client = idletown.create_client(session_name)
    controller = idletown.create_game_controller(client)
    await idletown.perform_full_run(controller)


async def test_readme_example(session_name):
    # Late import so that the autouse fixtures run first
    import examples.readme_example.readmeexample as readmeexample

    client = readmeexample.create_client(session_name)
    await readmeexample.run_example(client)
