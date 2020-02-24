from typing import *
import asyncio
import aiohttp
import random
import uuid
import html
import royalnet.commands as rc
import royalnet.utils as ru
from ..tables import TriviaScore
from royalnet.backpack.tables.users import User


class TriviaCommand(rc.Command):
    name: str = "trivia"

    aliases = ["t"]

    description: str = "Manda una domanda dell'OpenTDB in chat."

    syntax = "[credits|scores]"

    _letter_emojis = ["🇦", "🇧", "🇨", "🇩"]

    _medal_emojis = ["🥇", "🥈", "🥉", "🔹"]

    _correct_emoji = "✅"

    _wrong_emoji = "❌"

    _answer_time = 20

    # _question_lock: bool = False

    def __init__(self, interface: rc.CommandInterface):
        super().__init__(interface)
        self._answerers: Dict[uuid.UUID, Dict[str, bool]] = {}

    async def run(self, args: rc.CommandArgs, data: rc.CommandData) -> None:
        arg = args.optional(0)
        if arg == "credits":
            await data.reply(f"ℹ️ [c]{self.interface.prefix}{self.name}[/c] di [i]Steffo[/i]\n"
                             f"\n"
                             f"Tutte le domande vengono dall'[b]Open Trivia Database[/b] di [i]Pixeltail Games[/i],"
                             f" creatori di Tower Unite, e sono rilasciate sotto la licenza [b]CC BY-SA 4.0[/b].")
            return
        elif arg == "scores":
            trivia_scores = await ru.asyncify(data.session.query(self.alchemy.get(TriviaScore)).all)
            strings = ["🏆 [b]Trivia Leaderboards[/b]\n"]
            for index, ts in enumerate(sorted(trivia_scores, key=lambda ts: -ts.score)):
                if index > 3:
                    index = 3
                strings.append(f"{self._medal_emojis[index]} {ts.user.username}: [b]{ts.score:.0f}p[/b]"
                               f" ({ts.correct_answers}/{ts.total_answers})")
            await data.reply("\n".join(strings))
            return
        # if self._question_lock:
        #     raise rc.CommandError("C'è già un'altra domanda attiva!")
        # self._question_lock = True
        # Fetch the question
        async with aiohttp.ClientSession() as session:
            async with session.get("https://opentdb.com/api.php?amount=1") as response:
                j = await response.json()
        # Parse the question
        if j["response_code"] != 0:
            raise rc.CommandError(f"OpenTDB returned an error response_code ({j['response_code']}).")
        question = j["results"][0]
        text = f'❓ [b]{question["category"]}[/b]\n' \
               f'{html.unescape(question["question"])}'
        # Prepare answers
        correct_answer: str = question["correct_answer"]
        wrong_answers: List[str] = question["incorrect_answers"]
        answers: List[str] = [correct_answer, *wrong_answers]
        if question["type"] == "multiple":
            random.shuffle(answers)
        elif question["type"] == "boolean":
            answers.sort(key=lambda a: a)
            answers.reverse()
        else:
            raise NotImplementedError("Unknown question type")
        # Find the correct index
        for index, answer in enumerate(answers):
            if answer == correct_answer:
                correct_index = index
                break
        else:
            raise ValueError("correct_index not found")
        # Add emojis
        for index, answer in enumerate(answers):
            answers[index] = f"{self._letter_emojis[index]} {html.unescape(answers[index])}"
        # Create the question id
        question_id = uuid.uuid4()
        self._answerers[question_id] = {}

        # Create the correct and wrong functions
        async def correct(data: rc.CommandData):
            answerer_ = await data.get_author(error_if_none=True)
            try:
                self._answerers[question_id][answerer_.uid] = True
            except KeyError:
                raise rc.UserError("Tempo scaduto!")
            await data.reply("🆗 Hai risposto alla domanda. Ora aspetta un attimo per i risultati!")

        async def wrong(data: rc.CommandData):
            answerer_ = await data.get_author(error_if_none=True)
            try:
                self._answerers[question_id][answerer_.uid] = False
            except KeyError:
                raise rc.UserError("Tempo scaduto!")
            await data.reply("🆗 Hai risposto alla domanda. Ora aspetta un attimo per i risultati!")

        # Add question
        keyboard: List[rc.KeyboardKey] = []
        for index, answer in enumerate(answers):
            if index == correct_index:
                keyboard.append(rc.KeyboardKey(interface=self.interface,
                                               short=self._letter_emojis[index],
                                               text=answers[index],
                                               callback=correct))
            else:
                keyboard.append(rc.KeyboardKey(interface=self.interface,
                                               short=self._letter_emojis[index],
                                               text=answers[index],
                                               callback=wrong))
        async with data.keyboard(text=text, keys=keyboard):
            await asyncio.sleep(self._answer_time)
        results = f"❗️ Tempo scaduto!\n" \
                  f"La risposta corretta era [b]{answers[correct_index]}[/b]!\n\n"
        for answerer_id in self._answerers[question_id]:
            answerer = data.session.query(self.alchemy.get(User)).get(answerer_id)
            if answerer.trivia_score is None:
                ts = self.interface.alchemy.get(TriviaScore)(user=answerer)
                data.session.add(ts)
                await ru.asyncify(data.session.commit)
            previous_score = answerer.trivia_score.score
            if self._answerers[question_id][answerer_id]:
                results += self._correct_emoji
                answerer.trivia_score.correct_answers += 1
            else:
                results += self._wrong_emoji
                answerer.trivia_score.wrong_answers += 1
            current_score = answerer.trivia_score.score
            score_difference = current_score - previous_score
            results += f" {answerer}: [b]{current_score:.0f}p[/b] ({score_difference:+.0f}p)\n"
        await data.reply(results)
        del self._answerers[question_id]
        await ru.asyncify(data.session.commit)
        # self._question_lock = False
