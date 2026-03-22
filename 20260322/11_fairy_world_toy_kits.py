from abc import ABC, abstractmethod


# Productインターフェース（全部品が実装）
class Product(ABC):
    @abstractmethod
    def getCosts(self):
        pass


# 各部品クラス
class Head(Product):
    def __init__(self, description, difficulty, cost):
        self.description = description
        self.difficulty = difficulty
        self.cost = cost

    def getCosts(self):
        return self.cost

    def __str__(self):
        return self.description


class Body(Product):
    def __init__(self, description, difficulty, cost, sound=None):
        self.description = description
        self.difficulty = difficulty
        self.cost = cost
        self.sound = sound

    def getCosts(self):
        return self.cost

    def makeSound(self):
        if self.sound:
            return self.sound
        return "..."

    def __str__(self):
        return self.description


class LeftArm(Product):
    def __init__(self, description, difficulty, cost):
        self.description = description
        self.difficulty = difficulty
        self.cost = cost

    def getCosts(self):
        return self.cost

    def __str__(self):
        return self.description


class RightArm(Product):
    def __init__(self, description, difficulty, cost):
        self.description = description
        self.difficulty = difficulty
        self.cost = cost

    def getCosts(self):
        return self.cost

    def __str__(self):
        return self.description


class Legs(Product):
    def __init__(self, description, difficulty, cost):
        self.description = description
        self.difficulty = difficulty
        self.cost = cost

    def getCosts(self):
        return self.cost

    def walk(self):
        return "歩く"

    def __str__(self):
        return self.description


# 抽象ファクトリー
class HumanoidToyKitFactory(ABC):
    @abstractmethod
    def createHead(self): pass
    @abstractmethod
    def createBody(self): pass
    @abstractmethod
    def createLeftArm(self): pass
    @abstractmethod
    def createRightArm(self): pass
    @abstractmethod
    def createLegs(self): pass


# 具象ファクトリー1: サイバーヴァンパイア
class CyberVampireKitFactory(HumanoidToyKitFactory):
    def createHead(self):
        return Head("光る目を持つ頭部（牙スイッチ付き）", 3, 500)

    def createBody(self):
        return Body("黒いマントの胴体", 2, 800, "コウモリの音")

    def createLeftArm(self):
        return LeftArm("爪付きの左腕", 2, 300)

    def createRightArm(self):
        return RightArm("血の入ったカップを持つ右腕", 3, 400)

    def createLegs(self):
        return Legs("冷徹な二本の足", 1, 300)


# 具象ファクトリー2: ロボット
class RobotKitFactory(HumanoidToyKitFactory):
    def createHead(self):
        return Head("LEDアンテナ付きの頭部", 4, 600)

    def createBody(self):
        return Body("メタルアーマーの胴体", 3, 900, "ビープ音")

    def createLeftArm(self):
        return LeftArm("ドリル付きの左腕", 4, 500)

    def createRightArm(self):
        return RightArm("レーザーガン付きの右腕", 4, 500)

    def createLegs(self):
        return Legs("キャタピラ式の足", 3, 400)


# 具象ファクトリー3: ウェアウルフ
class WerewolfKitFactory(HumanoidToyKitFactory):
    def createHead(self):
        return Head("鋭い牙を持つ狼の頭部", 2, 400)

    def createBody(self):
        return Body("毛皮に覆われた胴体", 2, 700, "遠吠え")

    def createLeftArm(self):
        return LeftArm("鉤爪の左腕", 2, 300)

    def createRightArm(self):
        return RightArm("鉤爪の右腕", 2, 300)

    def createLegs(self):
        return Legs("筋肉質な二本の足", 1, 250)


# おもちゃ組み立て関数
def createAHumanoidToyByKit(factory):
    head = factory.createHead()
    body = factory.createBody()
    left_arm = factory.createLeftArm()
    right_arm = factory.createRightArm()
    legs = factory.createLegs()

    parts = [head, body, left_arm, right_arm, legs]
    total_cost = sum(p.getCosts() for p in parts)
    max_difficulty = max(p.difficulty for p in parts)

    print("=== おもちゃ完成！ ===")
    print(f"頭部: {head}")
    print(f"胴体: {body}")
    print(f"左腕: {left_arm}")
    print(f"右腕: {right_arm}")
    print(f"両足: {legs}")
    print(f"音: {body.makeSound()}")
    print(f"動作: {legs.walk()}")
    print(f"難易度: {max_difficulty}/5")
    print(f"合計金額: {total_cost}円")
    print()

    return parts


# テスト
print("【サイバーヴァンパイアキット】")
createAHumanoidToyByKit(CyberVampireKitFactory())

print("【ロボットキット】")
createAHumanoidToyByKit(RobotKitFactory())

print("【ウェアウルフキット】")
createAHumanoidToyByKit(WerewolfKitFactory())
